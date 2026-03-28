import React    from "react";

const Navbar: React.FC = () => {
    return (
        <div className="container h-16 w-30  bg-slate-400  text-xl text-white  rounded-full flex  flex-row items-center justify-between   ">

            <a href="/" className="hover:underline p-10" > Home  </a>
            <a href="/about" className="hover:underline p-10" > About </a>
            <a href="/projects" className="hover:underline p-10" > Projects </a>
            <a href="/articles" className="hover:underline  p-10" > Articles  </a>
            <a href="/contact" className="hover:underline  p-10"  > Contact </a> 
            
        </div>
    );
};
export default Navbar;