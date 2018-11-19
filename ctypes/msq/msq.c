/*
 * Compile:
 *  MSVC: cl /LD msq.c /o msq.dll
 *  GCC: gcc -fPIC -shared msq.c -o msq.dll
 */
#include <stdlib.h>
#include <math.h>

#ifdef MSVC_VER
 #define DLL_EXPORT __declspec( dllexport )
#else
 #define DLL_EXPORT
#endif

typedef struct point_s {
    double x;
    double y;
} point_t;

typedef struct test_s {
    char *pSentence;
    int nr_points;
    point_t *points;
    double *distances;
} test_t;

#ifdef __cplusplus
extern "C" {
#endif

char *increment_string(char *str, int n)
{}
    for (int i = 0; str[i]; i++)
        str[i] = str[i] + n;
    return str;
}

void generate_points(test_t *test, int n)
{
    point_t *pt = calloc(n+1, sizeof(point_t));

    for (int i = 0; i < n; i++) {
        pt[i].x = rand();
        pt[i].y = rand();
    }
    
    test->points = pt;
    test->nr_points = n;
}

void distance_between_points(test_t *test)
{
    int nb = test->nr_points;
    double *distances = calloc(nb * nb + 1, sizeof(double));

    for (int i = 0; i < nb; i++) {
        for (int j = 0; j < nb; j++) {
            distances[i * nb + j] = sqrt( (test->points[j].x - test->points[i].x) * (test->points[j].x - test->points[i].x) +
                (test->points[j].y - test->points[i].y) * (test->points[j].y - test->points[i].y) );
        }
    }

    test->distances = distances; 
}

#ifdef __cplusplus
}
#endif
