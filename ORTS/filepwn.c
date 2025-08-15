#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>

void filepwn() {
    const char *logo = 
        "  _____.__.__                              \n"
        "_/ ____\\__|  |   ____ ________  _  ______  \n"
        "\\   __\\|  |  | _/ __ \\____ \\ \\/ \\/ /    \\ \n"
        " |  |  |  |  |_\\  ___/|  |_> >     /   |  \\ \n"
        " |__|  |__|____/\\___  >   __/ \\/\\_/|___|  / \n"
        "                    \\/|__|              \\/  \n";
    
    printf("%s", logo);
}

void enumerate_directory(const char *path, const char *keyword) {
    struct dirent *entry;
    DIR *dp = opendir(path);

    if (dp == NULL) {
        perror("opendir");
        return;
    }

    while ((entry = readdir(dp))) {
        
        if (entry->d_type == DT_REG && strstr(entry->d_name, keyword) != NULL) {
            printf("%s\n", entry->d_name);
        }
    }

    closedir(dp);
}

int main(int argc, char *argv[]) {
    filepwn(); 
    const char *path = "/"; 
    const char *keyword = argc > 1 ? argv[1] : ""; 

    if (strlen(keyword) == 0) {
        printf("Please provide a keyword to search for.\n");
        return 1;
    }

    enumerate_directory(path, keyword);
    return 0;
}
