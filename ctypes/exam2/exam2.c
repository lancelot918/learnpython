/*
 * Compile:
 *  MSVC: cl /LD msq.c /o msq.dll
 *  GCC: gcc -fPIC -shared msq.c -o msq.dll
 */
#include <stdio.h>
#include <string.h>

#ifdef MSVC_VER
 #define DLL_EXPORT __declspec( dllexport )
#else
 #define DLL_EXPORT
#endif

typedef struct example_s {
    char *data;
    int len;
    double *doubles;
    int count;
} example_t;

#ifdef __cplusplus
extern "C" {
#endif

DLL_EXPORT void func(example_t *p)
{
    strcpy(p->data, "hello from exam2.dll!");
    for(int  i = 0; i< p->count; i++) {
        p->doubles[i] *= 0.9;
    }
}

#ifdef __cplusplus
}
#endif
