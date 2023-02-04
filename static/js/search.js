function search(filter , td){
for(i = 0;i<td.length;i++){
if(td[i].innerHTML.toLocaleUpperCase().indexOf(filter)> -1){
    return true
}
}
return false
}
function searchFunction(){
    let input , filter , table , tr , td , j;
    input = document.getElementById("searchbox");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName('tr');

    for(j=1 ; j < tr.length ; j ++){
        td = tr[j].getElementsByTagName("td")
        if(search(filter , td)){
            tr[j].style.display = "";
        }
        else {
            tr[j].style.display = "none";
        }
    }
}