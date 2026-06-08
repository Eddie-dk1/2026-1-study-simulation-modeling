
include(joinpath(@__DIR__, "..", "src", "Lab06.jl"))
using .Lab06

println(petri_sir_step(990, 10, 0, 0.32, 0.11, 1000))
