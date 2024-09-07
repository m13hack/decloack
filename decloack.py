import click
from modules.browser_exploit import check_browser_vulnerabilities
from modules.data_analysis import analyze_data
from modules.honeypot import setup_honeypot
from modules.traffic_analysis import perform_traffic_analysis

# ANSI escape codes for colors
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_CYAN = "\033[96m"
COLOR_RESET = "\033[0m"

# Display the options menu
def show_menu():
    print(f"\n{COLOR_GREEN}-----------------------------------------{COLOR_RESET}")
    print(f"{COLOR_GREEN}          De-cloack Menu                   {COLOR_RESET}")
    print(f"{COLOR_GREEN}-------------------------------------------{COLOR_RESET}")
    print(f"{COLOR_GREEN}Select an option by entering the corresponding number(s):{COLOR_RESET}")
    
    options = [
        "Browser Exploit",
        "Data Analysis",
        "Honeypot Setup",
        "Traffic Analysis"
    ]

    # Display the options as a numbered list
    for i, option in enumerate(options, 1):
        print(f"{COLOR_GREEN}{i}. {option}{COLOR_RESET}")

    # Get user input for selecting the options
    selected_options = input(f"\n{COLOR_YELLOW}Enter the number(s) separated by commas (e.g., 1,2): {COLOR_RESET}")

    # Split and convert the input into a list of integers
    return [int(num.strip()) for num in selected_options.split(",")]

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """\033[92mWelcome to the De-cloack CLI\033[0m"""
    
    # ASCII Art with Hacker Style Aesthetic
    print(f"""
 {COLOR_BLUE}/$$$$$$$                              /$$                               /$$      {COLOR_RESET}
{COLOR_CYAN}| $$__  $$                            | $$                              | $$      {COLOR_RESET}
{COLOR_BLUE}| $$  \\ $$  /$$$$$$           /$$$$$$$| $$  /$$$$$$   /$$$$$$   /$$$$$$$| $$   /$${COLOR_RESET}
{COLOR_CYAN}| $$  | $$ /$$__  $$ /$$$$$$ /$$_____/| $$ /$$__  $$ |____  $$ /$$_____/| $$  /$$/{COLOR_RESET}
{COLOR_BLUE}| $$  | $$| $$$$$$$$|______/| $$      | $$| $$  \\ $$  /$$$$$$$| $$      | $$$$$$/ {COLOR_RESET}
{COLOR_CYAN}| $$  | $$| $$_____/        | $$      | $$| $$  | $$ /$$__  $$| $$      | $$_  $$ {COLOR_RESET}
{COLOR_BLUE}| $$$$$$$/|  $$$$$$$        |  $$$$$$$| $$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$ \\  $$ {COLOR_RESET}
{COLOR_YELLOW}|_______/  \\_______/         \\_______/|__/ \\______/  \\_______/ \\_______/|__/  \\__/{COLOR_RESET}
                                                                           {COLOR_YELLOW} ||Ver:1.0.0||                             {COLOR_RESET}          
                                                                                    

                                                                                    {COLOR_YELLOW} By:                              {COLOR_RESET}
                                                                                    {COLOR_YELLOW}        ______      ______        {COLOR_RESET}
                                                                                    {COLOR_YELLOW}       |  _  \\___  |  _  \\       {COLOR_RESET}
                                                                                    {COLOR_YELLOW}       | | | ( _ ) | | | |       {COLOR_RESET}
                                                                                    {COLOR_YELLOW}       | | | / _ \\/ | | |        {COLOR_RESET}
                                                                                    {COLOR_BLUE}         |/ / (_>  < |/ /        {COLOR_RESET}
                                                                                    {COLOR_YELLOW}       |___/ \\___/\\ /___/        {COLOR_RESET}
                                                                                                    
    """)

    if ctx.invoked_subcommand is None:
        # If no command is invoked, run menu_mode as the default behavior
        menu_mode()

@cli.command()
def menu_mode():
    """\033[91mLaunch De-cloack in Menu Mode\033[0m"""
    print(f"{COLOR_RED}-------------------------------------------------{COLOR_RESET}")
    print(f"{COLOR_RED}   De-cloack: Decloaking Hidden Entities   {COLOR_RESET}")
    print(f"{COLOR_RED}-------------------------------------------------{COLOR_RESET}")
    
    while True:
        try:
            selected_options = show_menu()

            # Execute the corresponding actions for the selected options
            for option in selected_options:
                if option == 1:
                    browser_exploit()
                elif option == 2:
                    data_analysis()
                elif option == 3:
                    honeypot()
                elif option == 4:
                    traffic_analysis()
                else:
                    print(f"{COLOR_RED}Invalid option: {option}{COLOR_RESET}")
                    
            # Ask the user if they want to continue
            proceed = input(f"\n{COLOR_YELLOW}Do you want to continue? (y/n): {COLOR_RESET}").lower()
            if proceed != 'y':
                print(f"\n{COLOR_RED}Exiting De-Cloack. Goodbye!!!!{COLOR_RESET}")
                break
        except ValueError:
            print(f"{COLOR_RED}Invalid input. Please enter numbers only.{COLOR_RESET}")

@cli.command()
def traffic_analysis():
    """\033[91mPerform Traffic Correlation Analysis\033[0m"""
    try:
        perform_traffic_analysis()
    except Exception as e:
        click.echo(f"{COLOR_RED}Error: {e}{COLOR_RESET}")

@cli.command()
def browser_exploit():
    """\033[91mCheck for Browser Vulnerabilities\033[0m"""
    try:
        check_browser_vulnerabilities()
    except Exception as e:
        click.echo(f"{COLOR_RED}Error: {e}{COLOR_RESET}")

@cli.command()
def honeypot():
    """\033[91mSet up a Honeypot\033[0m"""
    try:
        setup_honeypot()
    except Exception as e:
        click.echo(f"{COLOR_RED}Error: {e}{COLOR_RESET}")

@cli.command()
def data_analysis():
    """\033[91mCross-reference Data from Multiple Sources\033[0m"""
    try:
        analyze_data()
    except Exception as e:
        click.echo(f"{COLOR_RED}Error: {e}{COLOR_RESET}")

if __name__ == "__main__":
    try:
        cli()
    except KeyboardInterrupt:
        click.echo(f"{COLOR_RED}Process Interrupted!{COLOR_RESET}")
    except Exception as e:
        click.echo(f"{COLOR_RED}Unexpected Error: {e}{COLOR_RESET}")
