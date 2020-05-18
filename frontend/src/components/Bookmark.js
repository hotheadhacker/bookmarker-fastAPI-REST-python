import React, { Fragment, useState } from 'react';
// import { Link } from 'react-router-dom';
import axios from 'axios';

const Bookmark = () => {
  const [formData, setFormData] = useState({
    url: '',
    label: ''
  });

  const { url, label } = formData;

  const onChange = e =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const onSubmit = async e => {
    e.preventDefault();

    try {
      const res = await axios.post(`/bookmark?url=${url}&label=${label}`);
      console.log(res.data);
    } catch (err) {
      console.error(err.response.data);
    }
  };

  return (
    <Fragment>
      <div className='container'>
        <center>
          <form className='form myForm col-8' onSubmit={e => onSubmit(e)}>
            <div className='wrapper m-4'>
              <div className='row'>
                <input
                  className='form-control border-dark'
                  placeholder='Enter URL'
                  type='url'
                  name='url'
                  value={url}
                  onChange={e => onChange(e)}
                  required
                />
              </div>
              <div className='row mt-2'>
                <input
                  className='form-control border-dark'
                  placeholder='Enter Label (optional)'
                  type='text'
                  name='label'
                  value={label}
                  onChange={e => onChange(e)}
                />
              </div>

              <center>
                <div className='row mt-2'>
                  <input
                    type='submit'
                    className='btn btn-success form-control'
                    value='Add'
                  />
                </div>
              </center>
            </div>
          </form>
        </center>
      </div>
    </Fragment>
  );
};

export default Bookmark;
