function fun_if() {
  i = document.getElementById('an_int').value
  if (i<0) {
    document.write(i + " is less than zero")
  }
  else if (i>0) {
    document.write(i + " is bigger than zero")
  }
  else {
    document.write(i + " is equal to zero")
  }
}
