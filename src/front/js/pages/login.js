import React, { useContext, useState } from "react";
import { Context } from "../store/appContext"; //para obtener el contexto de la aplicación
//import { Link, useNavigate } from "react-router-dom"; //para manejar la navegación dentro de la aplicación.

const Login = () => {
  const {store, actions} = useContext(Context);

  const [user, setUser] = useState({});
  
  const handleChange = (e) => {
    setUser({...user, [e.target.name]: e.target.value})
  }

  const handleClick = () => {
    actions.register(user);
  }
  

  return (
    <>
    <input type="text" placeholder="name" name="name" onChange={handleChange}/>
    <input type="text" placeholder="email" name="email" onChange={handleChange}/>
    <input type="password" placeholder="password" name="password" onChange={handleChange}/>
    <button type="button" onClick={handleClick}>ENVIAR</button>
    </>
  );
};

export default Login;