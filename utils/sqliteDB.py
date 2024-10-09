import aiosqlite
import os
import asyncio

class SqliteHandle:
    def __init__(self, db_path):
        """初始化数据库连接，指定文件路径"""
        self.db_path = os.path.abspath(db_path)  # 转换为绝对路径
        self.db_exists = os.path.exists(db_path)

    async def connect(self):
        """连接到数据库"""
        self.connection = await aiosqlite.connect(self.db_path)
        self.cursor = await self.connection.cursor()
        
        if self.db_exists:
            await self.on_file_exists()
        else:
            await self.on_file_not_exists()

    async def on_file_exists(self):
        """处理文件存在的情况（事件 1）"""
        pass  # 可根据需要添加逻辑

    async def on_file_not_exists(self):
        """处理文件不存在的情况（事件 2）"""
        # 标的列表
        await self.create_table("security", {
            "id": "INTEGER PRIMARY KEY",
            "symbol": "TEXT",
            "name_cn": "TEXT",
            "name_en": "TEXT",
            "name_hk": "TEXT"
        })
        await self.create_index("security", "symbol")

    async def create_table(self, table_name, columns, callback = None):
        """创建表，并使用回调函数检查表是否存在"""
        if callback is not None:
            if await callback(table_name):
                print(f"表 {table_name} 已存在，不创建.")
                return
        
        columns_with_types = ', '.join(f"{col} {typ}" for col, typ in columns.items())
        await self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_with_types})")
        await self.connection.commit()

    async def table_exists(self, table_name):
        """检查表是否存在"""
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"
        await self.cursor.execute(query, (table_name,))
        result = await self.cursor.fetchone()
        return result is not None

    async def create_index(self, table_name, column_name):
        """创建普通索引"""
        await self.cursor.execute(f"CREATE INDEX IF NOT EXISTS idx_{column_name} ON {table_name} ({column_name})")
        await self.connection.commit()
    
    async def add_column(self, table_name, column_name, column_type):
        """追加字段到表中"""
        await self.cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")
        await self.connection.commit()

    async def insert_data(self, table_name, data):
        """插入数据，支持动态字段"""
        columns = ', '.join(data.keys())
        placeholders = ', '.join('?' for _ in data)
        await self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", tuple(data.values()))
        await self.connection.commit()

    async def update_data(self, table_name, set_values, condition):
        """更新数据，支持动态字段"""
        set_clause = ', '.join(f"{col} = ?" for col in set_values.keys())
        condition_clause = ' AND '.join(f"{col} = ?" for col in condition.keys())
        values = list(set_values.values()) + list(condition.values())
        await self.cursor.execute(f"UPDATE {table_name} SET {set_clause} WHERE {condition_clause}", values)
        await self.connection.commit()

    async def save_data(self, table_name, data, conditions):
        """根据条件判断是否存在，存在则更新，不存在则新增"""
        condition_clauses = ' AND '.join(f"{key} = ?" for key in conditions.keys())
        condition_values = tuple(conditions.values())
        
        existing = await self.query_data(f"SELECT * FROM {table_name} WHERE {condition_clauses}", condition_values)
        
        if existing:
            # 更新数据
            await self.update_data(table_name, data, conditions)
        else:
            # 插入数据
            await self.insert_data(table_name, data)

    async def delete_data(self, table_name, condition):
        """删除数据"""
        condition_clause = ' AND '.join(f"{col} = ?" for col in condition.keys())
        values = list(condition.values())
        await self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition_clause}", values)
        await self.connection.commit()

    async def query_data(self, query, params=()):
        """查询数据"""
        await self.cursor.execute(query, params)
        return await self.cursor.fetchall()

    async def close(self):
        """关闭数据库连接"""
        await self.cursor.close()
        await self.connection.close()
    
    async def db_handle(self, callback):
        await self.connect()
        await callback()  # 执行回调函数
        await self.close()

# 使用示例
async def main():
    db_path = "longbridge.db"  # 指定数据库文件路径
    db = SqliteHandle(db_path)

    await db.connect()

    # 插入数据，支持动态字段
    await db.insert_data("users", {"name": "Alice", "age": 30})
    await db.insert_data("users", {"name": "Bob", "age": 25})

    # 更新数据，支持动态字段
    await db.update_data("users", {"age": 31}, {"name": "Alice"})

    # 删除数据
    await db.delete_data("users", {"name": "Bob"})

    # 查询数据
    results = await db.query_data("SELECT * FROM users")
    for row in results:
        print(row)

    # 关闭连接
    await db.close()

if __name__ == "__main__":
    """
    使用示例1
    """
    # asyncio.run(main())

    """
    使用示例2
    """
    db_path = "longbridge.db"  # 指定数据库文件路径
    db = SqliteHandle(db_path)
    async def execute_db():
        await db.insert_data("users", {"name": "Bob", "age": 25})
        await db.insert_data("users", {"name": "Bob", "age": 25})
        await db.insert_data("users", {"name": "Bob", "age": 25})
        await db.insert_data("users", {"name": "Bob", "age": 25})
        await db.insert_data("users", {"name": "Bob", "age": 25})

    for i in range(100):
        asyncio.run(db.db_handle(execute_db))
