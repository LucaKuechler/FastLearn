# Forensik-Workshop for SpringCamp 2023

## Setup
1. Clone the repository and change into it:
    ```bash
    git clone https://github.com/LucaKuechler/FastLearn && cd FastLearn/forensik-workshop
    ```

2. Delete the .git folder from the repository, we don't need it.
    ```
    rm -rf .git/
    ```

3. Extract the wordpress source code
    ```
    unzip forensics.zip
    ```

&nbsp;
## Remember
* Never execute any .exe files!

&nbsp;
## Investigation
1. What version of wordpress has been used?
    * Format: x.x.x
    * Answer:

2. Find the last date a file has been edited:
    * Format: Okt 21 05:25:46 2012
    * Answer:

3. Which files habe been edited on that specific date:
    * Hint 1: Some files like .jpg can be exclueded.
    * Hint 2: The perfect answer contains 11 Files.
    * List of file paths:
        * &lt;first answer&gt;
        * ...

4. Look througt the found files, which look sketchy to you?
    * List of file paths:
        * &lt;first answer&gt;
        * ...

5. Which file contains the php-reverse-shell?
    * Format: filename.extension
    * Answer: 

6. Where did the hacker place the dangerous html file?
    * Format: filepath/filename.extension
    * Answer: 

7. What happens when you open up that html file in your Browser?
    * Answer: 

8. Is the file an archive, if yes unpack it.
    * Remember: 7z is a very cool tool!
    * Format: yes/no
    * Answer:

9. Mhh. I don't know what to do now. Maybe the riddle that was shown to you can help.
    * Hint: Name of the Linux Tool
    * Answer: 

10. What is the flag you found inside the reverse-shell and the binary?
    * Format: HTB{asdf-addf-a12f-aSxf}
    * Answer: 
