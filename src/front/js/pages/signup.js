import React, { useState, useContext } from "react";
import { Context } from "../store/appContext"; //parea administrar el estado globlal 






const Login = () => {
    const [email,setEmail] = useState(""); //para crear dos variables de estado
    const [password, setPassword] = useState("");  //Estas variables se inicializan con valores iniciales vacios ("").
    const { store, actions } = useContext(Context);  // para acceder al contexto de la aplicación y obtener el objeto store y actions(ya que son las que modifican)

} 