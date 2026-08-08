from hijridate import Gregorian

def convert_gregorian_to_hijri(year: int, month: int, day: int) -> str:
    """Converts a Gregorian date into a formatted Hijri date string."""
    hijri_date = Gregorian(year, month, day).to_hijri()
    return f"{hijri_date.day} {hijri_date.month_name()} {hijri_date.year} AH"

def main():
    print("=" * 50)
    print("        GREGORIAN TO HIJRI DATE CONVERTER       ")
    print("        Format Example: 24/08/2026 (DD/MM/YYYY) ")
    print("=" * 50)
    
    try:
        # Prompting user for structured date input
        day = int(input("Enter Day   [DD]   (e.g., 24) : "))
        month = int(input("Enter Month [MM]   (e.g., 08) : "))
        year = int(input("Enter Year  [YYYY] (e.g., 2026): "))
        
        # Perform calculation
        result = convert_gregorian_to_hijri(year, month, day)
        
        print("-" * 50)
        print(f"Gregorian Input : {day:02d}/{month:02d}/{year}")
        print(f"Hijri Output    : {result}")
        print("=" * 50)
        
    except ValueError:
        print("\n[Error] Invalid input! Please enter numbers only (e.g., Day: 24, Month: 8, Year: 2026).")
    except Exception as e:
        print(f"\n[Error] Conversion failed: {e}")

if __name__ == "__main__":
    main()