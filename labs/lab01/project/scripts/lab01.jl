
include(joinpath(@__DIR__, "..", "src", "Lab01.jl"))
using .Lab01

t, u = exponential_growth(0.3, 10.0)
println("steps=", length(t), " final=", round(u[end]; digits=3))
