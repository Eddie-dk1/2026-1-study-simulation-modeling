
module Lab08

export total_rate

total_rate(s::Int, i::Int, beta::Float64, gamma::Float64, n::Int) = beta * s * i / n + gamma * i

end
