
include(joinpath(@__DIR__, "..", "src", "Lab04.jl"))
using .Lab04

println(round(infection_probability(0.28, 3); digits=4))
