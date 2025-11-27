# CLI Apps with MySQL

## Dependencies

- Python 3.13
- uv 0.9.8

## Activating Python Virtual Enviroments

```python
uv sync
```

## Dumping Database

### Loginning MySQL terminal

```bash
mysql -u root -p
```

### Dumping DB files

- [BMI Application Dumpfile](/bmi/docs/bmiapp_schema.sql)
- [Todo Application Dumpfile](/todo/docs/todo.sql)

#### Dumping

```sql
SOURCE /path/to/your/project/dump.dmp
```

## Execute projects

### school-cli-app

```bash
uv run python -m school.main
```

### bmi-cli-app

```bash
uv run python -m bmi.src.menu_menu
```

### todo-cli-app

```bash
uv run python -m todo.src.main_menu
```
