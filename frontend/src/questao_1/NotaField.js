
function NotaField({ maxNota, value, onChange }) {
    function onChangeValue (event) {
        const nota = event.target.value

        if (nota <= maxNota) {
            onChange(nota)
        }
    }

    return (
      <div>
        <input
            type={'number'}
            value={value}
            onChange={onChangeValue}
        />
      </div>
    );
  }
  
export default NotaField;
