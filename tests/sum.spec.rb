# Ruby with RSpec

class Sum
  def sum(a, b)
    a + b
  end
end


describe Sum do
  subject { Sum.new }

  it 'should sum 2 numbers' do
   expect(subject.sum(1, 2).to eq 3
  end
end
