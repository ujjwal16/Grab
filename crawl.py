from sys import argv
import source_link
import utility
while True:
	seed=raw_input("Enter seed link in proper format ")
	depth=int(input("Enter depth for search operation "))
	seed=seed
	visited=[]
	depth_0=[]
	check=0
	log2=open("visited.txt",'w')
	link_list,depth_0=utility.source(seed,seed,depth)
	visited=utility.merge(visited,link_list)
	visited=list(set(visited))
	log2.write("\n".join(visited))	
	log2.close()
	search=raw_input("Enter main keywords to search or No to skip searching process ")
	if search.lower()!="no":
		search_list=utility.form_list(search)
		print search_list
		s=int(input("Enter 1 to perform strict search or 0 to perform lenient search "))
		if s==1:
			strict=utility.strict_list(visited,search_list)
			print "\n".join(strict)
			if not strict:
				check=1
		else:
			lenient=utility.lenient_list(visited,search_list)
			print "\n".join(lenient)
			if not lenient:
				check=1

	if check!=1:

		resp=int(input("Do you want to extract desired pdf(enter 1 for yes and 0 for no ) "))
		if resp==1 and s==1:
			file_name=raw_input("Enter folder with complete path ")
			utility.download(strict,file_name)
			#print "Thank you for using crawler"
		elif resp==1 and s==0:
			file_name=raw_input("Enter folder with complete path ")
			utility.download(lenient,file_name)
			#print "Thank you for using crawler"
		else:
			pass
			#print "Thank you for using crawler"
	else :
		print "No desired link found\n"
		#print "Thank you for using crawler"
	again=raw_input("Enter yes to repeat process or press any key to exit ")
	if again.lower()!="yes":
		break
print "Thank you for using crawler"

#print visited




