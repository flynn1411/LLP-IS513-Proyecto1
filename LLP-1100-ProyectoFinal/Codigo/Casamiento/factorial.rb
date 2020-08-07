/comment
    # ! Método factorial.
    # * Permite calcular la multiplicación de n*(n-1)*(n-2)*...*(n-k), donde n-k >= 1
    # @author swd
    # @version 0.1

uncomment/

def factorial n
    if n < 2
        return 1
    end
    n*factorial(n-1)
end

n = 5

print ("El factorial de ")

puts factorial(n)