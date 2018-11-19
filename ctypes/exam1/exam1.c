/*
 * Compile:
 *  MSVC: cl /LD exam1.c /o exam1.dll
 *  GCC: gcc -fPIC -shared exam1.c -o exam1.dll
 */

#ifdef MSVC_VER
 #define DLL_EXPORT __declspec( dllexport )
#else
 #define DLL_EXPORT
#endif

#ifdef __cplusplus
extern "C" {
#endif

DLL_EXPORT int get_inc(unsigned int n)
{
    return n+1;
}

DLL_EXPORT int get_array_value(int a[], int idx)
{
    return a[idx];
}

#ifdef __cplusplus
}
#endif
