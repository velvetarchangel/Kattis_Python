long zeros(long n) {
  long trailing_zeroes = 0;
  for(long i = 5; n/i >= 1; i *= 5) {
    trailing_zeroes += n/i;
    }
  
  return trailing_zeroes;
}
