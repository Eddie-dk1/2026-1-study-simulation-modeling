
include(joinpath(@__DIR__, "..", "src", "Lab08.jl"))
using .Lab08

println(round(total_rate(180, 6, 0.5, 0.18, 186); digits=3))
