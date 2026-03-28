export default function Home() {
    return (
        <div>
            <form action={"/"}>

                <h1 className="text-center"> login Page</h1>
                <div className="container w-20 border p-4 rounded-3 mx-auto">
                    <div>

                        <label htmlFor="username">Username</label><br />
                        <input type="text" id="username" name="username" />
                    </div>
                    <div>
                    </div>
                    <label htmlFor="password">Password</label><br />
                    <input type="password" id="password" name="password"></input>

                    <div className="py-2">
                        <button className="btn btn-primary">Login</button>
                    </div>
                </div>


            </form>

        </div >
    );
}