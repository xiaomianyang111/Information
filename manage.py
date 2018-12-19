from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import db, current_app
from info import model

app = current_app("development")
# 设置应用程序在命令行启动与数据库迁移
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)
print(app.url_map)

if __name__ == "__main__":
    manager.run()