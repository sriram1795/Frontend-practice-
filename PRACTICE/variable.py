name = "Sriram"
Age = 22
Study = "Master"
percentage = 9.3
is_different = True
name="sri"
# Data types
# list
Vm_boys_hostel = [3,6500,"water","food",["veg","nonveg"]]
#Dictinary
expenses = {
    "hostelfee" : 6500,
    "institutefee" : "30k",
    "extraexpenses" : "2k",
    "extrexpenses":{"tea":300,"biriyani" :1000, "curries" :300, "traveling" :400},
    "coursestructure":["python","HTML","CSS","SQL","react","django","APIcreation"],
    "hostel":("food","bed","water","cleaning","washingmachine")
}
#tuple
details=("Sriram",22,"masters",)
details=("sai",20,"10th")
#earge=list(Vm_boys_hostel.values())+dict(expenses.values())+tuple(details.values())
print("learning python fulstack course in 10k codders and staying in Vm's Hostel")
print(name,Age,Study,percentage,Vm_boys_hostel,expenses,details,is_different)
print(type(expenses))
print(type(Vm_boys_hostel))
print(expenses["hostelfee"])
print(expenses["extrexpenses"["curries"]])