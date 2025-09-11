#include <stdio.h>
#include <windows.h>
#include <lm.h>

#pragma comment(lib, "netapi32.lib")

void printUserInfo() {
    DWORD dwEntries = 0;
    DWORD dwTotalEntries = 0;
    DWORD dwResumeHandle = 0;
    USER_INFO_0 *pUserInfo = NULL;

    NET_API_STATUS nStatus = NetUserEnum(NULL, 0, FILTER_NORMAL_ACCOUNT, (LPBYTE*)&pUserInfo, MAX_PREFERRED_LENGTH, &dwEntries, &dwTotalEntries, &dwResumeHandle);

    if (nStatus == NERR_Success) {
        for (DWORD i = 0; i < dwEntries; i++) {
            printf("User: %ws\n", pUserInfo[i].usri0_name);

            printf("  Enabled: %s\n", (pUserInfo[i].usri0_flags & UF_ACCOUNTDISABLE) ? "No" : "Yes");

            LOCALGROUP_MEMBERS_INFO_0 *pGroupInfo = NULL;
            DWORD dwGroupEntries = 0;
            DWORD dwTotalGroupEntries = 0;

            nStatus = NetUserGetLocalGroups(NULL, pUserInfo[i].usri0_name, 0, LG_INCLUDE_INDIRECT, (LPBYTE*)&pGroupInfo, MAX_PREFERRED_LENGTH, &dwGroupEntries, &dwTotalGroupEntries);

            if (nStatus == NERR_Success) {
                printf("  Groups: ");
                for (DWORD j = 0; j < dwGroupEntries; j++) {
                    printf("%ws ", pGroupInfo[j].lgrmi0_name);
                }
                printf("\n");
                NetApiBufferFree(pGroupInfo);
            } else {
                printf("  Groups: Unable to retrieve groups\n");
            }
            printf("\n");
        }
        NetApiBufferFree(pUserInfo);
    } else {
        printf("NetUserEnum failed with error: %d\n", nStatus);
    }
}

int main() {
    printUserInfo();
    return 0;
}
