#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <fcntl.h>
#define PORT 8080
#define BUFFER_SIZE 1024

void linfy() {
    const char *logo = 

" _ _        __        \n"
"| (_)_ __  / _| _     _ \n"
"| | | '_\\| |_|  | | | |\n"
"| | | | | |  _| | |_| |\n"
"|_|_|_| |_|_|   \\__ / |\n"
"                 ____/ \n";
    
    printf("%s", logo);
}

int create_server_socket() {
    int server_fd;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);

    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt))) {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    if (listen(server_fd, 3) < 0) {
        perror("listen");
        exit(EXIT_FAILURE);
    }

    return server_fd;
}

void handle_client(int client_socket) {
    char buffer[BUFFER_SIZE] = {0};
    read(client_socket, buffer, BUFFER_SIZE);
    
    char method[10], path[100];
    sscanf(buffer, "%s %s", method, path);

    char *file_path = path + 1;

    int file = open(file_path, O_RDONLY);
    if (file < 0) {
        const char *not_found = "HTTP/1.1 404 Not Found\r\n\r\nFile Not Found";
        send(client_socket, not_found, strlen(not_found), 0);
    } else {
        const char *header = "HTTP/1.1 200 OK\r\n\r\n";
        send(client_socket, header, strlen(header), 0);

        char file_buffer[BUFFER_SIZE];
        ssize_t bytes_read;
        while ((bytes_read = read(file, file_buffer, BUFFER_SIZE)) > 0) {
            send(client_socket, file_buffer, bytes_read, 0);
        }
        close(file);
    }

    close(client_socket);
}


int main() {
    linfy();
    int server_fd = create_server_socket();
    printf("Server is running on port %d\n", PORT);

    while (1) {
        int client_socket = accept(server_fd, NULL, NULL);
        if (client_socket < 0) {
            perror("accept");
            continue;
        }
        handle_client(client_socket);
    }

    close(server_fd);
    return 0;
}
