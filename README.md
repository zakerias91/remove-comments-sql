# Remove comments from a SQL file
This package removes comments from a SQL file.

It will remove comments that:
* Start with a slash and an asterisk and end with an asterisk and a slash. 
* Start with two hyphens. 
* Span multiple lines.

## Instructions
Please ensure Python is installed on your machine. Python does not come prepackaged with Windows.

Save the remove_comments.py file in a directory alongside the SQL file you wish to remove comments from. Then open a PowerShell or Command Prompt window in this location.

To run the script enter:

```
python remove_comments.py yoursqlfile.sql
```
This will create a .NOCOMMENTS file in your directory with the original SQL filename.
