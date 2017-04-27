int clog (void);
int ctan (void);
int casinh (void);
int cacosh (void);
int cabs (void);
int conj (void);
int csqrt (void);
int creal (void);
int cproj (void);
int cpow (void);
int csinh (void);
int catan (void);
int ctanh (void);
int ccosh (void);
int cimag (void);
int casin (void);
int carg (void);
int csin (void);
int cexp (void);
int ccos (void);
int cacos (void);
int catanh (void);
#ifdef _MSC_VER
#pragma function(cabs)
#pragma function(cacos)
#pragma function(cacosh)
#pragma function(carg)
#pragma function(casin)
#pragma function(casinh)
#pragma function(catan)
#pragma function(catanh)
#pragma function(ccos)
#pragma function(ccosh)
#pragma function(cexp)
#pragma function(cimag)
#pragma function(clog)
#pragma function(conj)
#pragma function(cpow)
#pragma function(cproj)
#pragma function(creal)
#pragma function(csin)
#pragma function(csinh)
#pragma function(csqrt)
#pragma function(ctan)
#pragma function(ctanh)
#endif
int main (void) {
  cabs();
  cacos();
  cacosh();
  carg();
  casin();
  casinh();
  catan();
  catanh();
  ccos();
  ccosh();
  cexp();
  cimag();
  clog();
  conj();
  cpow();
  cproj();
  creal();
  csin();
  csinh();
  csqrt();
  ctan();
  ctanh();
  return 0;
}
