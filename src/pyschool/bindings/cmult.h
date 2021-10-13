// cmult.h
// Source code reference:
// https://github.com/realpython/materials/blob/master/python-bindings/cmult.h

#ifdef _MSC_VER
#define EXPORT_SYMBOL __declspec(dllexport)
#else
#define EXPORT_SYMBOL
#endif

float cmult(int int_param, float float_param);

// EXPORT_SYMBOL float cmult(int int_param, float float_param);