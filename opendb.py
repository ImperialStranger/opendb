import typer, sqlite3


opendb = typer.Typer()
DATABASE = 'opendb.db'


conn = sqlite3.connect(DATABASE);
cursor = conn.cursor()


def save_connection(name, engine, host, port, db, user, password):
    try:
        cursor.execute(f"""INSERT INTO connections(name, engine, host, port, db, user, password) 
        VALUES({name}, {engine}, {host}, {port}, {db}, {user}, {password});""")
        return True
    except:
        return False


@opendb.command()
def main():
    print("OpenDB Universal Database Accessor v0.1")


@opendb.command()
def add_connection(name: str = typer.Option(...), engine: str = typer.Option(...), host: str = typer.Option(...), port: int = typer.Option(...), database: str = typer.Option(...), user: str = typer.Option(...), password: str = typer.Option(...)):
    output = save_connection(name, engine, host, port, database, user, password)
    if output:
        msg = typer.style(f"Connection {name} has successfully added.", bg=typer.colors.GREEN)
        typer.echo(msg)
    else:
        msg = typer.style(f"Error", bg=typer.colors.RED)
        typer.echo(msg)  


if __name__ == "__main__":
    opendb()
