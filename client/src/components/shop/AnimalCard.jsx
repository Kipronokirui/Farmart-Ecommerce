import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { increment, removeItem, productQtyInCartSelector } from '../../store/features/CartSlice'
import { toast } from 'react-toastify'
import { useNavigate } from 'react-router-dom'

export default function AnimalCard({animal}) {
    const qty = useSelector(state=>productQtyInCartSelector(state, animal.id))
    const dispatch = useDispatch()
    const navigate = useNavigate()

    const handleCartAddition = async(animal) => {
        dispatch(increment(animal))
        toast.success('Animal succesfully added to cart')
        navigate('/cart')
    }

    const handleCartRemoval = async(animal) => {
        dispatch(removeItem(animal))
        toast.success('Animal succesfully removed from cart')
    }

    function AddToCart(){
        if(!qty){
            return(
                <button 
                    onClick={() => handleCartAddition(animal)}
                    className="text-white bg-green-600 hover:bg-green-700 
                    font-medium rounded-lg text-sm px-5 py-2 text-center"
                >
                    Add to cart
                </button>
            )
        }
        return(
            <button 
                onClick={() => handleCartRemoval(animal)}
                className="text-white bg-red-600 hover:bg-red-700 
                font-medium rounded-lg text-sm px-5 py-2 text-center"
            >
                Remove from cart
            </button>
        )
    }
  return (
    <>
    <div className="rounded overflow-hidden shadow-lg">
        <div className="relative">
            <a href={`/animal/${animal.id}`}>
                <img className="w-full h-40"
                    src={animal.cover_photo}
                    alt={animal.type}
                />
                <div
                    className="hover:bg-transparent transition duration-300 
                    absolute bottom-0 top-0 right-0 left-0 bg-gray-900 opacity-25"
                >
                </div>
            </a>
            <a href={`/animal/${animal.id}`}>
                <div
                    className="absolute bottom-0 left-0 bg-green-600 px-4 py-2 
                    text-white text-sm hover:bg-green-700 
                    transition duration-500 ease-in-out"
                >
                    {animal.type}
                </div>
            </a>
        </div>
        <div className="px-3 py-4">
            <a 
                href={`/animal/${animal.id}`}
                className="font-semibold text-lg inline-block 
                hover:text-green-600 transition duration-500 ease-in-out"
            >
                Breed: {animal.breed}
            </a>
            <p className="text-gray-500 text-sm">
                Age: {animal.age}
            </p>
            <p className="text-gray-500 text-sm">
                Quantity: {animal.quantity}
            </p>
            <p className="text-gray-500 text-sm">
                {animal.description}
            </p>
        </div>
        <div className='px-3 pb-2'>
            <p 
                className="pb-1 font-semibold text-lg inline-block"
            >
                Price: Ksh. {animal.price}
            </p>
            <AddToCart />
        </div>
    </div>
    </>
  )
}
