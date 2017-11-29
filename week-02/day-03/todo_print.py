# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected outpt:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo

todoText = "My todo:\n - Buy milk\n - Download games\n     - Diablo"

print(todoText)

todoText = """My todo:
 - Buy milk
 - Download games
     - Diablo"""

print(todoText)