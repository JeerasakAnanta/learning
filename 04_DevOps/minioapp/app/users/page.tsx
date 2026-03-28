interface User {
    id: number;
    name: string;
    email: string;

}

export default async function UsersPage() {

    // fecth data  from external API  
    const res = await fetch('https://jsonplaceholder.typicode.com/users');
    const users: User[] = await res.json();
    return (
        <div className="">
          {users}
        </div>
    )
}
