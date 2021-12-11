const Head = () => {
  return (
    <div className="d-flex w-100 justify-content-between  align-items-center p-3">
      <div className="title">
        <span className="semi">SEMI</span>{" "}
        <span className="live">
          LIVE <span className="floatDot">.</span>
        </span>
      </div>
      <div className="search d-flex">
        <input type="text" />
      </div>
      <div>
        <i class="fas fa-user"></i>
        <span className="username">USERNAME</span>
      </div>
    </div>
  );
};

export default Head;
