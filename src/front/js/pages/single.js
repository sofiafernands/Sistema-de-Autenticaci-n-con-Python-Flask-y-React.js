import React, { useState, useEffect, useContext } from "react";
import PropTypes from "prop-types";
import { Link, useParams } from "react-router-dom";//importamos el hooks useParams
import { Context } from "../store/appContext";


//aqui iria el detalle de cada card 

export const Single = props => {
	const { store, actions } = useContext(Context);
	const params = useParams();
	useEffect ( ()=>{
		if (params.type === "characters") {
			actions.fetchCharacter(params.theid)
		console.log(store)
		}
		else if (params.type === "planets") {
			actions.fetchPlanet(params.theid)
		console.log(store)
		}

	},[])
	
	const getDetail = ( ) => {
		if (params.type==="characters"){
			return(
				<>
				<h2><b>Name:</b> {store.character.name}</h2>
				<br/>
				<h4><b>Birthday:</b> {store.character.birth_year}</h4>
				<br/>
				<h4><b>Hair color:</b> {store.character.hair_color}</h4>
				<br/>
				<h4><b>Height:</b>  {store.character.height}</h4>
				<br/>
				<h4><b>Eye color:</b>  {store.character.eye_color}</h4>
				</>

			)
		}
		else if ( params.type==="planets"){
			return (
				<> 
				<h2><b>Name: </b> {store.planet.name}</h2>
				<br/>
				<h4><b>Climate: </b>{store.planet.climate}</h4>
				<br/>
				<h4><b>Diameter: </b>{store.planet.diameter}</h4>
				<br/>
				<h4><b>Terrain: </b>{store.planet.terrain}</h4>
				<br/>
				<h4><b>Population: </b>{store.planet.population}</h4>
				<br/>
				<h4><b>Gravity: </b>{store.planet.gravity}</h4>

				</>
			)
		}
		else if ( params.type==="vehicles"){
			return (
				<> 
				<h2><b>Name:</b> {store.vehicle.name}</h2>
				
				</>
			)
		}
		

	}


	return (
<div className="jumbotron" style={{padding:"20px",display: "flex",justifyContent:"space-between"}}>

  <div>
  <img src={`https://starwars-visualguide.com/assets/img/${params.type}/${params.theid}.jpg`}

         className="card"
         style={{ height: "500px", width: "400px",borderRadius:"20px" }}
         alt="..." />
		 <Link to="/">
				<span className="btn btn-primary btn-lg" href="#" role="button" style={{marginTop:"20px",background:"#434943",border:"0px"}}>
					Back home
				</span>
			</Link>
  </div>
		 <span style={{color:"white"}}>
			{ getDetail()}
		</span>
</div>



	);
};

Single.propTypes = {
	match: PropTypes.object //object son los elementos que hay dentro del array de fetch
};