#include <winsock2.h> 
#include <ws2tcpip.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <io.h>

#pragma comment(lib, "ws2_32.lib") 

#define PORT 8080
#define BUFFER_SIZE 1024

void winfy() {
    const char *logo = 

"          _        __         \n"
"__      _(_)_ __  / _|_   _  \n"
"\\ \\ /\\ / / | '_ \\| |_| | | | \n"
" \\ V  V /| | | | |  _| |_| | \n"
"  \\_/\\_/ |_|_| |_|_|  \\__, | \n"
"                      |___/  \n";

    printf("%s", logo);
}


void handle_client(SOCKET client_socket) {
    char buffer[BUFFER_SIZE] = {0};
    recv(client_socket, buffer, BUFFER_SIZE, 0);
    
    char method[10], path[100];
    sscanf(buffer, "%s %s", method, path);
    char *file_path = path + 1;

    FILE *file = fopen(file_path, "rb");
    if (file == NULL) {
        const char *not_found = "HTTP/1.1 404 Not Found\r\n\r\nFile Not Found";
        send(client_socket, not_found, strlen(not_found), 0);
    } else {
        const char *header = "HTTP/1.1 200 OK\r\n\r\n";
        send(client_socket, header, strlen(header), 0);

        char file_buffer[BUFFER_SIZE];
        size_t bytes_read;
        while ((bytes_read = fread(file_buffer, 1, BUFFER_SIZE, file)) > 0) {
            send(client_socket, file_buffer, bytes_read, 0);
        }
        fclose(file);
    }

    closesocket(client_socket);
}

int main() {
    winfy();
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        printf("WSAStartup failed: %d\n", WSAGetLastError());
        return 1;
    }

    SOCKET server_socket = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr));
    listen(server_socket, 3);

    printf("Server is running on port %d\n", PORT);

    while (1) {
        SOCKET client_socket = accept(server_socket, NULL, NULL);
        if (client_socket != INVALID_SOCKET) {
            handle_client(client_socket);
        }
    }

    closesocket(server_socket);
    WSACleanup();
    return 0;
}
