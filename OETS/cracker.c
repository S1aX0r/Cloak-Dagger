#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>

void cracker() {
    const char *logo = 
"                       _                \n     "
"    ___ _ __ __ _  ___| | _____ _ __     \n    "
"   / __| '__/ _` |/ __| |/ / _ \\ '__|    \n    "
"  | (__| | | (_| | (__|   <  __/ |        \n   "
"   \\___|_|  \\__,_|\\___|_|\\_\\___|_|   \n    ";  
    printf("%s", logo);
}

void hash_password(const char *password, unsigned char *outputBuffer) {
    SHA256((unsigned char*)password, strlen(password), outputBuffer);
}

void hex_to_bytes(const char *hex, unsigned char *bytes) {
    for (size_t i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        sscanf(hex + 2 * i, "%2hhx", &bytes[i]);
    }
}

void dictionary_attack(const char *hash, const char *wordlist) {
    FILE *file = fopen(wordlist, "r");
    if (!file) {
        perror("Could not open wordlist file");
        return;
    }

    char password[256];
    unsigned char hashBuffer[SHA256_DIGEST_LENGTH];
    unsigned char targetHash[SHA256_DIGEST_LENGTH];
    hex_to_bytes(hash, targetHash);

    while (fgets(password, sizeof(password), file)) {
        password[strcspn(password, "\n")] = 0; 
        hash_password(password, hashBuffer);

        if (memcmp(hashBuffer, targetHash, SHA256_DIGEST_LENGTH) == 0) {
            printf("Password found: %s\n", password);
            fclose(file);
            return;
        }
    }

    printf("Password not found in the wordlist.\n");
    fclose(file);
}

void brute_force_attack(const char *hash, int length) {
    if (length <= 0 || length > 8) { 
        printf("Length must be between 1 and 8.\n");
        return;
    }

    unsigned char hashBuffer[SHA256_DIGEST_LENGTH];
    unsigned char targetHash[SHA256_DIGEST_LENGTH];
    hex_to_bytes(hash, targetHash);

    char password[length + 1];
    password[length] = '\0';

    for (int i = 0; i < (1 << (length * 8)); i++) {
        for (int j = 0; j < length; j++) {
            password[j] = (i >> (j * 8)) & 0xFF; 
        }
        hash_password(password, hashBuffer);

        if (memcmp(hashBuffer, targetHash, SHA256_DIGEST_LENGTH) == 0) {
            printf("Password found: %s\n", password);
            return; 
        }
    }

    printf("Password not found in brute-force attempt.\n");
}

int main(int argc, char *argv[]) {
    cracker(); 

    if (argc < 4) {
        printf("Usage: %s <hash> <mode> <wordlist/length>\n", argv[0]);
        return 1;
    }

    const char *hash = argv[1];
    const char *mode = argv[2];

    if (strcmp(mode, "dict") == 0) {
        const char *wordlist = argv[3];
        dictionary_attack(hash, wordlist);
    } else if (strcmp(mode, "brute") == 0) {
        int length = atoi(argv[3]); 
        brute_force_attack(hash, length);
    } else {
        printf("Invalid mode. Use 'dict' or 'brute'.\n");
    }

    return 0;
}
