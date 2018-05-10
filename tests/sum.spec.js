// Node + Jest

class Sum {
  sum(a, b) {
    return a + b;
  }
}

describe('Sum', () => {
  it('should sum 2 numbers', () => {
    const sum = new Sum();
    expect(sum.sum(1,2).toBe(3);
  });
});
