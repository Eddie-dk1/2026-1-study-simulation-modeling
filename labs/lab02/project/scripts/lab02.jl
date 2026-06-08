
include(joinpath(@__DIR__, "..", "src", "Lab02.jl"))
using .Lab02

s, i, r = sir_step(0.99, 0.01, 0.0, 0.36, 0.12, 0.5)
println(round(s; digits=4), " ", round(i; digits=4), " ", round(r; digits=4))
