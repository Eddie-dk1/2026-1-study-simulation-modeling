
module Lab06

export petri_sir_step

function petri_sir_step(s::Int, i::Int, r::Int, beta::Float64, gamma::Float64, population::Int)
    new_inf = min(s, round(Int, beta * s * i / population))
    new_rec = min(i, round(Int, gamma * i))
    return s - new_inf, i + new_inf - new_rec, r + new_rec
end

end
