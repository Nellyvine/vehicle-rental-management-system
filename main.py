# Main Entry Point for Vehicle Rental Management System,
# Handle authentication(signup/login) and main program loop.

from main_system import MainSystem

def main():

# Main function that runs the entire system
    system = MainSystem()

# Authentication phase, user must sign up or login
    authenticated = system.authentication_menu()

    if not authenticated:
# User chose to exit or failed to authenticate after max attempts
        return

# Main program loop, only runs after successful login
    running = True
    while running:
        try:
            system.display_menu()
            choice = input("\nEnter your choice (1-6): ").strip()

            if choice == '6':
                system.exit_system()
                running = False
            else:
                running = system.handle_user_choice(choice)

        except KeyboardInterrupt:
            print("\n\nSystem interrupted by user.")
            system.exit_system()
            running = False

        except Exception as e:
            print("\nUnexpected error:", str(e))
            print("Please try again or contact system administrator.")
            system.pause()


if __name__ == "__main__":
    main()

