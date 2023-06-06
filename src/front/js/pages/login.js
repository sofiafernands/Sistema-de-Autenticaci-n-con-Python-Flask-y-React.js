import React, { useContext, useState } from "react";
import { Context } from "../store/appContext"; //para obtener el contexto de la aplicación
import { Link, useNavigate } from "react-router-dom"; //para manejar la navegación dentro de la aplicación.

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { actions } = useContext(Context);

  let navigate = useNavigate(); 
  //
//para manejar el envío del formulario cuando se hace clic en el botón "Entrar".
  const handleSubmit = async (e) => {
    e.preventDefault(); //(evitar recargar la página)
    let loginUser = await actions.login(email, password); // "await" para esperar a que se complete antes de continuar.

  };

  return (
    <div className="bg-fondo vh-100 ">
      <h1 className=" text-center pt-3">Acceder</h1>
      <div className="d-flex justify-content-center align-items-center h-50 d-inline-block">
        <form onSubmit={handleSubmit} className="col-10 col-md-5">
          <div className="mb-3">
            <label htmlFor="exampleInputEmail1" className="form-label ">
              Email*
            </label>
            <input
              type="email"
              className="form-control"
              id="exampleInputEmail1"
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div className="mb-3">
            <label htmlFor="exampleInputPassword1" className="form-label">
              Contraseña*
            </label>
            <input
              type="password"
              className="form-control"
              id="exampleInputPassword1"
              onChange={(e) => setPassword(e.target.value)} // almacenar y mantener actualizado el valor del campo
            />
          </div>
          <div className="d-grid mt-3">
            <button type="submit" className="btn btn-primary">
              Entrar
            </button>
          </div>
          <div className="d-grid mt-3">
            <Link to="/signup" className="text-white text-decoration-none btn btn-primary">
              Crear nuevo usuario
            </Link>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;