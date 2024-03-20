class lcg:
  def __init__(self, seed, a=1, c=0, m=2**64-1):
      self.seed = seed
      self.a = a
      self.c = c
      self.m = m
      self.current_val = seed
      self.counter = 0

  def roll(self):
      self.current_val = (self.a*self.current_val + self.c) % self.m
      self.counter += 1
      return self.current_val

  def roll_norm(self):
      return self.roll()/self.m

  def roll_byte(self):
      return self.roll() % 0x100

def lcg_cypher(text: bytearray, seed: int) -> bytearray:
  out = bytearray()
  key = lcg(seed)
  for i in text:
      out.append(i ^ key.roll_byte())
  return out
  #TODO: Check that you can encrypt and decrypt messages
  #TODO: succesfully.

def main():
  with open("to_encrypt.txt", "r") as file:
    ptext = file.read().encode()
  with open("encrypted.bin", "wb") as f:
    f.write(lcg_cypher(bytearray(ptext), 0xDEADBEEF))

  with open("encrypted.bin", "rb") as f:
    ctext = f.read()
  with open("decrypted.txt", "w") as f:
    f.write(lcg_cypher(ctext, 0xDEADBEEF).decode())


if __name__ == '__main__':
  main()