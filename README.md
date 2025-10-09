# CLI Apps with MySQL

## Dependencies

- Python 3.13

## Activating Python Virtual Enviroments

```python
python3 -m venv .venv
source .venv/bin/activate
```

## Installing Python Modules

```bash
pip install -r requirements.txt
```

## Dumping Database

### Loginning MySQL terminal

```bash
mysql -u root -p
```

### Dumping DB file

#### School-cli-app

```sql
DROP DATABASE IF EXISTS school;
CREATE DATABASE school;
USE school;
SOURCE /path/to/your/project/db/school.dmp
```

#### Bmi-cli-app

```sql
DROP DATABASE IF EXISTS bmiapp;
CREATE DATABASE bmiapp;
USE bmiapp;
SOURCE /path/to/your/project/bmi-cli-app/docs/bmiapp.dmp
```

#### Todo-cli-app

```sql
DROP DATABASE IF EXISTS 23010025_exam_db;
CREATE DATABASE 23010025_exam_db;
USE 23010025_exam_db;
SOURCE /path/to/your/project/bmi-cli-app/docs/23010025_exam_db.dmp
```

## Execute projects

- school-cli-app

  ```bash
  python.exe /path/to/your/project/school-cli-app/main_menu.py
  ```

- bmi-cli-app

  ```bash
  python.exe /path/to/your/project/bmi-cli-app/main_menu.py
  ```

- todo-cli-app

  ```bash
  python.exe /path/to/your/project/todo-cli-app/src/main_menu.py
  ```
