import datetime

def main():
  """Executes simple code and saves the output to a file with the current date and time."""
  current_datetime = datetime.datetime.now()
  formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")
  filename = f"output_{formatted_datetime}.txt"

  try:
    with open(filename, "w") as file:
      # Replace this with your desired code
      file.write("This is a sample output.\n")
      file.write(f"Current date and time: {current_datetime}\n")
      # End of your code
    print(f"Output saved to {filename}")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  main()
