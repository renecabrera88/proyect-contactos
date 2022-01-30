//aqui se escucha cuando a las clases btn-delete, en caso de ser apretada,
//se despliega una alert, para que confirme la eliminacion del registro
//sino se cancela borrado de registro en la base de dato
const btnDelete = document.querySelectorAll('.btn-delete')

if(btnDelete){
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn)=>{
        btn.addEventListener('click', (e)=>{
            if(!confirm('Estas seguro boorar registro?')){
                e.preventDefault();
            };
        });
    });
}