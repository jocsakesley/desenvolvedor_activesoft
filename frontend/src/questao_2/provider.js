import React, { useState } from "react";

export const Context = React.createContext({})

function Provider(props) {
    const [text, setTexto] = useState({
        text: "Texto"
    })

    return (
        <div>
            <Context.Provider value={{ text, setTexto }}>
                {props.children}
            </Context.Provider>
        </div>
    );
}

export default Provider;