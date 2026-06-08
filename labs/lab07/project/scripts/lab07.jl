
include(joinpath(@__DIR__, "..", "src", "Lab07.jl"))
using .Lab07

println(round(traffic_intensity(2.7, 1.0, 3); digits=3))
