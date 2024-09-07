import click
from modules.traffic_analysis import perform_traffic_analysis
from modules.browser_exploit import check_browser_vulnerabilities
from modules.honeypot import setup_honeypot
from modules.data_analysis import analyze_data

@click.group()
def cli():
    """\033[92mWelcome to the Tor De-Anonymizer CLI\033[0m"""
    
    # ASCII Art with Hacker Style Aesthetic
    print(r"""
 /$$$$$$$                              /$$                               /$$      
| $$__  $$                            | $$                              | $$      
| $$  \ $$  /$$$$$$           /$$$$$$$| $$  /$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$
| $$  | $$ /$$__  $$ /$$$$$$ /$$_____/| $$ /$$__  $$ |____  $$ /$$_____/| $$  /$$/
| $$  | $$| $$$$$$$$|______/| $$      | $$| $$  \ $$  /$$$$$$$| $$      | $$$$$$/ 
| $$  | $$| $$_____/        | $$      | $$| $$  | $$ /$$__  $$| $$      | $$_  $$ 
| $$$$$$$/|  $$$$$$$        |  $$$$$$$| $$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$ \  $$
|_______/  \_______/         \_______/|__/ \______/  \_______/ \_______/|__/  \__/

    ========================================
    ||   TOR DE-ANONYMIZATION TOOLKIT      ||
    ||       *Coded with Style*            ||
    ========================================
    ||  Select an option to proceed:       ||
    ========================================
    """)

@cli.command()
def traffic_analysis():
    """\033[91mPerform Traffic Correlation Analysis\033[0m"""
    try:
        perform_traffic_analysis()
    except Exception as e:
        click.echo(f"\033[91mError: {e}\033[0m")

@cli.command()
def browser_exploit():
    """\033[91mCheck for Browser Vulnerabilities\033[0m"""
    try:
        check_browser_vulnerabilities()
    except Exception as e:
        click.echo(f"\033[91mError: {e}\033[0m")

@cli.command()
def honeypot():
    """\033[91mSet up a Honeypot\033[0m"""
    try:
        setup_honeypot()
    except Exception as e:
        click.echo(f"\033[91mError: {e}\033[0m")

@cli.command()
def data_analysis():
    """\033[91mCross-reference Data from Multiple Sources\033[0m"""
    try:
        analyze_data()
    except Exception as e:
        click.echo(f"\033[91mError: {e}\033[0m")

if __name__ == "__main__":
    try:
        cli()
    except KeyboardInterrupt:
        click.echo("\033[91mProcess Interrupted!\033[0m")
